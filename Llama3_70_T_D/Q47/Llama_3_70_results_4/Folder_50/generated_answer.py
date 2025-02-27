import re

def palindromes_of_specific_lengths(s):
    s = s[36:93].lower()
    palindromes = set()
    for length in range(10, 36):
        patterns = [re.compile('.*(' + '[a-z]{' + str(length // 2) + '}' + '([a-z]).*\\\\2' + '[a-z]{' + str(length // 2 - 1) + '}' + ')') if length % 2 == 1 else re.compile('.*(' + '[a-z]{' + str(length // 2) + '}[a-z]?' + '[a-z]{' + str(length // 2) + '}' + ')')]
        for pattern in patterns:
            match = pattern.match(s)
            if match:
                palindrome = match.group(1)
                if palindrome.isalpha():
                    palindromes.add(palindrome)
    return palindromes