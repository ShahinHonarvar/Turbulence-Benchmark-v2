def palindrome_of_length_n(string, n=100):
    result = set()
    string = ''.join((c.lower() for c in string if c.isalpha()))
    if n % 2 == 1:
        for i in range(len(string) - n + 1):
            if string[i:i + n] == string[i:i + n][::-1]:
                result.add(string[i:i + n])
    else:
        for i in range(len(string) - n + 1):
            center = i + n // 2
            if string[center - 1:center + 1] == string[center - 1:center + 1][::-1]:
                result.add(string[i:i + n])
    return result