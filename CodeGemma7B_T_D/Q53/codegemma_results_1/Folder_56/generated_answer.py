def palindrome_of_length_at_least_n(str):
    str = str.lower()
    regex = '(?!.*[\\\\W\\\\d])(?<=\\\\w{84,})(\\\\w+)(?=\\\\w{84,})'
    palindromes = re.findall(regex, str)
    return set(palindromes)