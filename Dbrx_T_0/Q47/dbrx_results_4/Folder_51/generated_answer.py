def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(2, 9):
        for j in range(0, len(s) - i + 1):
            substring = s[j:j + i].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return {palindrome for palindrome in palindromes if 3 <= len(palindrome) <= 4}