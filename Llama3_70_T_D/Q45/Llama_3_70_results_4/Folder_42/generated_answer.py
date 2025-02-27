def palindromes_between_indices(s):
    s = s[6:10].lower()
    letters = ''.join(filter(str.isalpha, s))
    if len(letters) < 2:
        return set()
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            for j in range(i + length // 2 + 1, i + length):
                first_half = letters[i:j]
                second_half = first_half[::-1]
                if j + len(second_half) <= i + length:
                    palindrome = first_half + second_half
                    if len(palindrome) == length:
                        palindromes.add(palindrome)
    return palindromes