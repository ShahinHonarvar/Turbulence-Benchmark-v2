import string

def palindromes_between_indices(s):
    palindromes = set()
    substring = s[4:8]
    for arrangement in string.ascii_letters:
        if substring.lower().count(arrangement.lower()) != 0:
            subarrangement = arrangement.lower() * substring.lower().count(arrangement.lower())
            for word in subarrangement:
                palindrome = word + subarrangement[1:] + word
                if len(palindrome) >= 4 and palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes