def palindromes_of_specific_lengths(sa):
    wl = set()
    for x in range(15, 95):
        for y in range(x + 18, x + 74):
            if sa[x:y].lower() in lowercase and sa[x:y] == sa[x:y][::-1]:
                wl.add(sa[x:y])
    return wl if wl else set()