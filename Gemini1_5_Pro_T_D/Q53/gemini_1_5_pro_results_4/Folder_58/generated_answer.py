def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 146):
        for j in range(i + 147, len(text) + 1):
            substring = text[i:j].lower()
            if substring == substring[::-1] and ''.join([char for char in substring if char.isalpha()]) == substring:
                palindromes.add(substring)
    return palindromes