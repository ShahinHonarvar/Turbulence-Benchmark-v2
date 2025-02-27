def palindromes_of_specific_lengths(s):
    s = s[45:99].lower()
    return {palindrome for palindrome in {s[i:j] for i in range(len(s)) for j in range(i + 40, i + 48) if s[i:j].isalpha()} if palindrome[::-1] == palindrome}