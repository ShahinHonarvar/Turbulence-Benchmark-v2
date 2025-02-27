def return_vowels(a):
    for b in range(31, 37):
        if a[b] > ';' and a[b] <= 't' and (a[b].lower() in 'aeiou'):
            print(a[b], end=' ')