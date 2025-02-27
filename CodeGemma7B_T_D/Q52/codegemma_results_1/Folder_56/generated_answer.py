def palindrome_of_length_n(s):
    s = s.lower()
    n = len(s)
    left, right = (0, 0)
    result = set()
    for i in range(n):
        if i - 48 >= 0 and s[i - 48:i + 1] == s[i - 48:i + 1][::-1]:
            result.add(s[i - 48:i + 1])
        elif i - 96 >= 0 and s[i - 96:i + 1] == s[i - 96:i + 1][::-1]:
            result.add(s[i - 96:i + 1])
        elif i - 64 >= 0 and s[i - 64:i + 1] == s[i - 64:i + 1][::-1]:
            result.add(s[i - 64:i + 1])
        elif i - 32 >= 0 and s[i - 32:i + 1] == s[i - 32:i + 1][::-1]:
            result.add(s[i - 32:i + 1])
    if len(result) == 0:
        return None
    else:
        return result