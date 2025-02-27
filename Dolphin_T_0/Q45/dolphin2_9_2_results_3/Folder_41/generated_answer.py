def palindromes_between_indices(s):
    letters = set()
    for i in s[2:4]:
        letters.add(i.lower())
    palindromes = set()
    for i in range(len(s[2:4])):
        for j in range(i + 1, len(s[2:4]) + 1):
            sub_string = s[2:4][i:j]
            if len(sub_string) >= 3 and sub_string == sub_string[::-1]:
                palindrome = ''
                for letter in sub_string:
                    for i in range(ord(letter.lower()), ord(letter.lower()) + 27, 1):
                        palindrome += chr(i)
                palindromes.add(palindrome)
    return palindromes