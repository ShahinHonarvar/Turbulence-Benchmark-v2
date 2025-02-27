def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 5):
        for j in range(0, 26):
            palindrome = string[i:i + 6].lower()
            if palindrome == palindrome[::-1] and all((ch.isalpha() for ch in palindrome)) and (len(palindrome) == 6):
                palindromes.add(palindrome)
    return palindromes