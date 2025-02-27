def palindromes_between_indices(s):
    substring = s[3:7].lower()
    letters = [char for char in substring if char.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            first_half = letters[i:i + length // 2]
            second_half = letters[i + length // 2 + length % 2:i + length][::-1]
            if first_half == second_half:
                palindrome = ''.join(first_half + second_half + ([letters[i + length // 2]] if length % 2 != 0 else []))
                palindromes.add(palindrome)
    return palindromes