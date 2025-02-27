def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string)):
        if len(string[i:]) < 80:
            break
        substring = string[i:]
        if substring[:80] == substring[:40][::-1] == substring[40:80]:
            palindromes.add(substring[:80])
    return palindromes