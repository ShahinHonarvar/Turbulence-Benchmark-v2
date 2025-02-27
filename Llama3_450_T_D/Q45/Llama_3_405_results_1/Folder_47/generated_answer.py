import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:8] if c.isalpha()]
    unique_letters = list(set(letters))
    palindromes = set()
    for r in range(5, len(letters) + 1):
        for combination in itertools.combinations_with_replacement(unique_letters, r // 2):
            first_half = ''.join(combination)
            if r % 2 == 0:
                palindrome = first_half + first_half[::-1]
            else:
                for middle_letter in unique_letters:
                    palindrome = first_half + middle_letter + first_half[::-1]
                    palindromes.add(palindrome)
    return {palindrome for palindrome in palindromes if palindrome.isalpha()}