def palindrome_of_length_at_least_n(string):
    result = set()
    string = ''.join((c.lower() for c in string if c.isalpha()))
    n = len(string)
    for i in range(n):
        for j in range(i + 87, n + 1):
            substr = string[i:j]
            if substr == substr[::-1]:
                result.add(substr)
    return result