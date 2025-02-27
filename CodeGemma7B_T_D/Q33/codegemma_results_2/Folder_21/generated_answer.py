def return_vowels(s):
    l_vowel = [i for i in s[464:574] if 'a' < i <= 'g']
    if not l_vowel:
        return []
    else:
        return l_vowel