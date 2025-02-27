def palindromes_between_indices(s):
    s = s[1:9].lower()
    letters = [char for char in s if char.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            for j in range(i + length // 2):
                if letters[i + j] != letters[i + length - j - 1]:
                    break
            else:
                palindrome = ''.join(letters[i:i + length])
                palindromes.add(palindrome)
    return palindromes