from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[7:10] if char.isalpha()]

    def can_form_palindrome(letter_list):
        return len(letter_list) >= 4

    def generate_palindromes(letter_list):
        palindromes = set()
        for perm in set(permutations(letter_list)):
            for i in range(len(perm)):
                for j in range(i + 3, len(perm) + 1):
                    subset = perm[i:j]
                    if len(subset) >= 4:
                        palindrome = ''.join(subset)
                        if palindrome == palindrome[::-1]:
                            palindromes.add(palindrome)
        return palindromes
    return generate_palindromes(letters) if can_form_palindrome(letters) else set()