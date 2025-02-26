import itertools

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[2:4] if char.isalpha()]

    def generate_palindromes(current_letters):
        palindromes = set()
        for length in range(3, len(current_letters) * 2 + 1):
            for perm in itertools.permutations(current_letters, length // 2):
                half = list(perm)
                if length % 2 == 1:
                    for middle in set(current_letters):
                        palindrome = half + [middle] + half[::-1]
                        palindromes.add(''.join(palindrome))
                else:
                    palindrome = half + half[::-1]
                    palindromes.add(''.join(palindrome))
        return palindromes
    return generate_palindromes(letters)