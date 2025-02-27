def palindromes_between_indices(s):
    letters = [c.lower() for c in s[7:10] if c.isalpha()]
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            first_half = letters[i:i + length // 2]
            if length % 2 == 0:
                if first_half == letters[i + length // 2:i + length][::-1]:
                    palindrome = ''.join(first_half + letters[i + length // 2:i + length])
                    palindromes.add(palindrome)
            elif first_half == letters[i + length // 2 + 1:i + length][::-1]:
                palindrome = ''.join(first_half + [letters[i + length // 2]] + letters[i + length // 2 + 1:i + length])
                palindromes.add(palindrome)
    return palindromes