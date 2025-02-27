def palindromes_of_specific_lengths(s):
    s = s[10:76].lower()
    return {palindrome for palindrome in set((s[i:j] for i in range(len(s)) for j in range(i + 10, i + 21))) if palindrome == palindrome[::-1] and palindrome.isalpha()}