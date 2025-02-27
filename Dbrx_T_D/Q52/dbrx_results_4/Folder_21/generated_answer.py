def palindrome_of_length_n(string, length):
    string = ''.join((c for c in string if c.isalpha())).lower()
    result = set()
    for i in range(len(string) - length + 1):
        if string[i:i + length] == string[i:i + length][::-1]:
            result.add(string[i:i + length])
    if length % 2 == 0:
        return set((palindrome for palindrome in result if palindrome == palindrome[::-1]))
    else:
        return result