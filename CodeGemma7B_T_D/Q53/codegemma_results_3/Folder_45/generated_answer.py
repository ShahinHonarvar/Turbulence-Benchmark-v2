def palindrome_of_length_at_least_n(s):
    palindrome_set = set()
    for i in range(len(s)):
        for j in range(i + 3, len(s)):
            if s[i] == lower(s[j]):
                current_palindrome = s[i:j + 1]
                palindrome_set.add(current_palindrome)
    return palindrome_set