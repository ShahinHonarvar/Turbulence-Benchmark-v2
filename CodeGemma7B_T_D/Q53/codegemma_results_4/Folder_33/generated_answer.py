def palindrome_of_length_at_least_n(s):
    result = set()
    for i in range(len(s)):
        for j in range(i + 141, len(s) + 1):
            if s[i:j].lower() == s[i:j][::-1].lower():
                result.add(s[i:j])
    return result