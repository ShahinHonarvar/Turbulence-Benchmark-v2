def palindromes_between_indices(s):
    s = s[7:10].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            for j in range(i + length // 2 + 1):
                first_half = letters[i:j]
                second_half = first_half[::-1]
                if length % 2 == 1:
                    middle = letters[i + length // 2]
                else:
                    middle = ''
                palindrome = ''.join(first_half + [middle] + second_half)
                palindromes.add(palindrome)
    return palindromes