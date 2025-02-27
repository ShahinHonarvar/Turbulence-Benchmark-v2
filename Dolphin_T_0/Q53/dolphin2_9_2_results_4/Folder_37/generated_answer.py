def palindrome_of_length_at_least_n(s):
    s = s.lower()
    main_set = set()
    for i in range(len(s) - 66):
        sub = s[i:i + 67]
        if sub == sub[::-1] and sub.isalpha():
            main_set.add(sub)
    return main_set