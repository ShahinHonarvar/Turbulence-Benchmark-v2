from string import ascii_lowercase

def palindrome_of_length_n(str):
    if len(str) < 82:
        return set()
    letters = ''.join(ascii_lowercase)
    result = set()
    for a in range(len(str) - 82 + 1):
        for b in range(a + 82, len(str) + 1):
            temp = str[a:b]
            temp = temp.lower()
            if temp == temp[::-1] and temp.isalpha():
                result.add(temp)
    return result