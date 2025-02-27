def identical_elements(a, b):
    set((x for x in a[10:67] if x in set(b[10:67])))