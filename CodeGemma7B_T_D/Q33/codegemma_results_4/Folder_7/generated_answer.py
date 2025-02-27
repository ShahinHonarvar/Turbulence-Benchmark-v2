def return_vowels(s):
    vowels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    i = 0
    while i < len(s) and i <= 872:
        if s[i] in vowels and s[i] > 3 and (s[i] <= '>'):
            print(s[i], end=' ')
        i += 1
    print()