from itertools import permutations

def palindromes_between_indices(s):
    subset = s[3:6].lower()
    letters = [char for char in subset if char.isalpha()]

    def create_palindromes(available_letters):
        palindromes = set()
        for length in range(3, len(available_letters) + 1):
            for perm in set(permutations(available_letters, length)):
                perm_list = list(perm)
                if len(set(perm_list)) >= 3:
                    left = perm_list[:length // 2]
                    right = perm_list[length // 2 + length % 2:][::-1]
                    if left == right:
                        palindromes.add(''.join(perm_list))
        return palindromes
    return create_palindromes(letters)