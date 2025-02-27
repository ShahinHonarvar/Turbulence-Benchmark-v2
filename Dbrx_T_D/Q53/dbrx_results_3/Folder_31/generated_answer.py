def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s)):
        for j in range(max(0, i - 34), i + 1):
            if s[i] == s[j] or s[i].lower() == s[j].lower():
                current_palindrome = s[j:i + 1]
                if len(current_palindrome) >= 34 and current_palindrome == current_palindrome[::-1]:
                    palindromes.add(current_palindrome)
    return palindromes