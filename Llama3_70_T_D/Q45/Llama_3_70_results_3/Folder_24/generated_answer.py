def palindromes_between_indices(s):
    s = s[2:10].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        if length % 2 == 0:
            for i in range(len(letters) - length + 1):
                first_half = letters[i:i + length // 2]
                if first_half == first_half[::-1]:
                    palindrome = ''.join(first_half + first_half[::-1])
                    palindromes.add(palindrome)
        else:
            for i in range(len(letters) - length + 1):
                first_half = letters[i:i + (length - 1) // 2]
                if first_half == first_half[::-1]:
                    palindrome = ''.join(first_half + [letters[i + (length - 1) // 2]] + first_half[::-1])
                    palindromes.add(palindrome)
    return palindromes