def palindromes_between_indices(s):
    s = s[5:10].lower()
    letters = [char for char in s if char.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters) + 1):
            first_half = ''.join(letters[i:j])
            for k in range(len(letters)):
                for end in range(k + 1, len(letters) + 1):
                    second_half = ''.join(letters[k:end])
                    if len(first_half) + len(second_half) >= 6 and first_half == second_half[::-1]:
                        palindrome = first_half + second_half
                        palindromes.add(palindrome)
    return palindromes