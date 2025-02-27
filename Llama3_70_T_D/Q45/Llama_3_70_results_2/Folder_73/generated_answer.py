def palindromes_between_indices(s):
    s = s[3:7].lower()
    letters = [c for c in s if c.isalpha()]
    unique_letters = set(letters)
    palindromes = set()
    for letter in unique_letters:
        for i in range(letters.count(letter)):
            for other_letter in unique_letters:
                if other_letter != letter and letters.count(other_letter) > i:
                    palindrome = letter * (i + 1) + other_letter + letter * (i + 1)
                    palindromes.add(palindrome)
            if i == 0 and letters.count(letter) > 2:
                palindrome = letter * 3
                palindromes.add(palindrome)
    for length in range(4, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            substring = letters[i:i + length]
            if substring == substring[::-1]:
                palindrome = ''.join(substring)
                if len(set(palindrome)) == 1:
                    palindromes.add(palindrome)
    return palindromes