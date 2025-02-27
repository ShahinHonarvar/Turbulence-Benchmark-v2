def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    for i in range(len(s) - 317):
        segment = s[i:i + 318]
        if segment == segment[::-1]:
            result.add(segment)
    return result