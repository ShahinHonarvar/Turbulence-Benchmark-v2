def palindromes_between_indices(s):
    s = s[:6].lower()
    english_letters = [char for char in s if char.isalpha()]
    palindromes = set()
    for i in range(len(english_letters)):
        for j in range(i + 1, len(english_letters) + 1):
            first_half = ''.join(english_letters[i:j])
            for k in range(len(english_letters)):
                for end in range(k + 1, len(english_letters) + 1):
                    second_half = ''.join(english_letters[k:end])[::-1]
                    palindrome = first_half + second_half
                    if len(palindrome) >= 6 and palindrome == palindrome[::-1]:
                        palindromes.add(palindrome)
    return palindromes