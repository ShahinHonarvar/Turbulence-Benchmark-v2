def palindromes_between_indices(s):
    English_letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)] + [chr(i) for i in range(ord('a'), ord('z') + 1)]
    s = s[2:5]
    palindromes = set()
    for len_ in range(4, len(s) + 1):
        for i in range(len(s) - len_ + 1):
            substring = s[i:i + len_]
            if all((letter.lower() in English_letters for letter in substring)) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes