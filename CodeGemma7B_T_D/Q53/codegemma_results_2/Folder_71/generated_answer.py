def palindrome_of_length_at_least_n(a):
    result = set()
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            substring = a[i:j + 1]
            if substring == substring[::-1] and len(substring) >= 87 and (substring.lower() in a.lower()):
                result.add(substring)
    return result