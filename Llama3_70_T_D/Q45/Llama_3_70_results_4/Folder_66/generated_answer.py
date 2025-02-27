def palindromes_between_indices(s):
    s = s[:6].lower()
    english_letters = [char for char in s if char.isalpha()]
    if len(english_letters) < 5:
        return set()
    palindromes = set()
    for length in range(5, len(english_letters) + 1):
        for i in range(len(english_letters) - length + 1):
            first_half = english_letters[i:i + length // 2]
            second_half = english_letters[i + (length + 1) // 2:i + length][::-1]
            if first_half == second_half:
                palindrome = ''.join(first_half + second_half)
                if length % 2 == 1:
                    for char in set(english_letters[i + length // 2:i + (length + 1) // 2]):
                        palindromes.add(palindrome[:length // 2] + char + palindrome[length // 2:])
                else:
                    palindromes.add(palindrome)
    return palindromes