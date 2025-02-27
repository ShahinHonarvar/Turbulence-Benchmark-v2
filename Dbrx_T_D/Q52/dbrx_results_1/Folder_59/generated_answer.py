def palindrome_of_length_n(string, length=39):
    string = ''.join((c.lower() for c in string if c.isalpha()))
    if length > len(string) or length <= 0:
        return set()
    palindromes = {string[i:j] for i in range(len(string)) for j in range(len(string), -1, -1) if j - i == length and string[i:j] == string[i:j][::-1]}
    return palindromes