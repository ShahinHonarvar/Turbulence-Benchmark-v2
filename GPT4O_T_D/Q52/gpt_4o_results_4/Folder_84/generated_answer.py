def palindrome_of_length_n(s):
    result = set()
    s = ''.join([char for char in s if char.isalpha()]).lower()
    n = len(s)
    length = 131
    if n < length:
        return result
    for i in range(n - length + 1):
        substring = s[i:i + length]
        if substring == substring[::-1]:
            result.add(substring)
    return result