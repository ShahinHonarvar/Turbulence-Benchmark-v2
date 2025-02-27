def palindrome_of_length_n(string, n=318):
    string = ''.join((c.lower() for c in string if c.isalpha()))
    if n % 2 == 1:
        return {string[i:j] for i in range(len(string)) for j in range(i + n, i - n, -1) if string[i:j] == string[i:j][::-1]}
    else:
        return {string[i:j] for i in range(len(string)) for j in range(i + n, i - n, -1) if string[i:j] == string[i + 1:j - 1][::-1]}