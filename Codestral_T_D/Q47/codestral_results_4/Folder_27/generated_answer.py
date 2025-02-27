def palindromes_of_specific_lengths(s):
    substring = s[13:100].lower()
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 26, i + 30):
            if j > len(substring):
                break
            palindrome = substring[i:j]
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                palindromes.add(palindrome)
    return palindromes