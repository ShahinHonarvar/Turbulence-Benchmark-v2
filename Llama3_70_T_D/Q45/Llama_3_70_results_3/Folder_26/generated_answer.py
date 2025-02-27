def palindromes_between_indices(s):
    s = s.lower()
    substr = s[4:7]
    alphabets = [char for char in substr if char.isalpha()]
    palindromes = set()
    for i in range(len(alphabets)):
        for j in range(i + 1, len(alphabets)):
            for k in range(j + 1, len(alphabets) + 1):
                first_half = ''.join(alphabets[i:j])
                middle = ''.join(alphabets[j:k])
                palindrome = first_half + middle + first_half[::-1]
                if len(palindrome) >= 3:
                    palindromes.add(palindrome)
    return palindromes