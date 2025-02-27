def palindromes_of_specific_lengths(s):
    palindromes = set()
    substr = s[155:284]
    for i in range(len(substr)):
        for j in range(i + 104, i + 121):
            if j <= len(substr):
                sub = substr[i:j]
                if sub.lower() == sub[::-1].lower() and sub.isalpha():
                    palindromes.add(sub)
    return palindromes