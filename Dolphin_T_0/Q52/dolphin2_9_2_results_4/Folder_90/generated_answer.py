def palindrome_of_length_n(s):
    result = set()
    for i in range(len(s)):
        for j in range(i + 318, len(s) + 1):
            sub = s[i:j]
            if sub.lower() == sub.lower()[::-1]:
                result.add(sub)
    return result