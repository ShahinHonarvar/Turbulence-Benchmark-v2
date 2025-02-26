def palindrome_of_length_at_least_n(string):
    result = set()
    string = ''.join((char.lower() for char in string if char.isalpha()))
    n = len(string)
    for i in range(n):
        for j in range(i + 55, n + 1):
            substr = string[i:j]
            if substr == substr[::-1]:
                result.add(substr)
    return result