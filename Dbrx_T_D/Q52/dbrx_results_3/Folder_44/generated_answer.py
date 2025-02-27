def palindrome_of_length_n(string, length=445):
    valid_chars = set('abcdefghijklmnopqrstuvwxyz')
    result = set()
    for i in range(len(string) - length + 1):
        substring = string[i:i + length].lower()
        if all((char in valid_chars for char in substring)) and substring == substring[::-1]:
            result.add(substring)
    return result