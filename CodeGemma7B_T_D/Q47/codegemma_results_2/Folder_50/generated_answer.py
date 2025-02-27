def palindromes_of_specific_lengths(str):
    only_letters = ''.join(filter(str.isalpha, str))
    substring = only_letters[36:92 + 1]
    palindromes = set()
    for length in range(10, 35 + 1):
        for i in range(len(substring) - length + 1):
            palindrome = substring[i:i + length]
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                palindromes.add(palindrome)
    return palindromes