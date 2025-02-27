def palindrome_of_length_n(string, n=279):
    string = ''.join((c.lower() for c in string if c.isalpha()))
    if n % 2 == 1:
        length = n // 2 + 1
    else:
        length = n // 2
    result = set()
    for i in range(len(string) - length + 1):
        current = string[i:i + length]
        if n % 2 == 1 and current == current[::-1]:
            result.add(current + current[:-1][::-1])
        elif current == current[::-1]:
            result.add(current + current[::-1])
    return result