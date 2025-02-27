from collections import defaultdict

def palindromes_between_indices(string):
    letters = set((string[i].lower() for i in range(2, 7) if string[i].isalpha()))
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for letter in letters:
            perms = defaultdict(set)
            perms[letter].add(letter)
            for i in range(2, length + 1):
                for perm in perms[letter]:
                    for candidate in letters - set(perm):
                        new_perm = ''.join(sorted(perm + candidate))
                        perms[new_perm].add(candidate)
                        if len(new_perm) == length and new_perm == new_perm[::-1]:
                            palindromes.add(new_perm)
    return palindromes