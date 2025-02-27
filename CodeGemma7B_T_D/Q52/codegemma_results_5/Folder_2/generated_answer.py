def palindrome_of_length_n(s):
    result = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            is_palindrome = True
            for k in range(len(substring) // 2):
                if substring[k] != substring[len(substring) - k - 1]:
                    is_palindrome = False
                    break
            if is_palindrome and len(substring) == 147:
                result.add(substring)
    return result